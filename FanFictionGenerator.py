from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.cache import SQLiteCache
import langchain


class InitialPlotGenerator:
    def __init__(self):
        langchain.llm_cache = SQLiteCache(".langchain.db")

        self.llm = OpenAI(max_tokens=-1, temperature=0.7)
        self.TenNewPlots = LLMChain.from_string(
            self.llm, """Generate 10 plots for new episods of {seriesname}. Two or three sentences long.

1."""
        )

        self.CompatiblePlotCombination = LLMChain.from_string(self.llm, """We have a pool of pots for new episods for {seriesname}.
Plotpool:
{plotpool}

Create one new more entertaining plot by combining two plots from the pool, where they would fit together.
1.""")
        
    def generateInitialPlot(self, seriesname, UseCache=True):
        print("Generating initial Plot")
        self.llm.cache = UseCache
        plots = self.TenNewPlots.predict(seriesname=seriesname)
        print("Generated Plots: " + plots)
        
        compatibleCombination = self.CompatiblePlotCombination.predict(seriesname=seriesname, plotpool=plots)
        print("Compatible Combinations: " + compatibleCombination)

        return compatibleCombination


class FanFictionGenerator:
    def __init__(self):
        langchain.llm_cache = SQLiteCache(".langchain.db")

        self.llm = OpenAI(max_tokens=-1, temperature=0.7)
        self.initialStoryGenerator = LLMChain.from_string(
            self.llm, """Write a detailed Story for an new Episode of {seriesname}.
            The Plot is:
            {plot}
            
            Detailed Story:"""
        )

        self.problemGenerator = LLMChain.from_string(
            self.llm,
            """Between >>> and <<< is a new Story for {seriesname}

>>>
{story}
<<<

Where is the story unclear, where is not detailed enough?

Missing Details:""",
        )

        self.ProblemFixer = LLMChain.from_string(
            self.llm,
            """Between >>> and <<< is a new Story for {seriesname}
>>>
{story}
<<<
It has the following problems:
{problems}

Write new Details for the Story that fix the Problems. An Author will use this Details to rewrite the Story later.

Improvments:""",
        )

        self.NextVersion = LLMChain.from_string(
            self.llm,
            """Between >>> and <<< is a new Story for {seriesname}.
>>>
{story}
<<< 
The Critics found the following problems:
{problems}

The Authors found this Solution:
{solution}

Now Rewrite the Story with the new Details from the Solution.

New Version:""",
        )


    def generateInitialStory(self, seriesname, UseCache=True):
        print("Generating a new FanFiction")
        self.llm.cache = UseCache
        initialPlotGenerator = InitialPlotGenerator()
        plot = initialPlotGenerator.generateInitialPlot(seriesname, UseCache)

        story = self.initialStoryGenerator.predict(
            seriesname=seriesname, plot=plot)
        print("Generated initial Story: " + story)
        
        return story

    def improve(self, seriesname, story, count=1):

        for i in range(count):
            problems = self.problemGenerator.predict(
                story=story,
                seriesname=seriesname)
            print("Generated Problems:" + problems)

            solution = self.ProblemFixer.predict(
                story=story, seriesname=seriesname, problems=problems
            )
            print("Generated Solution: " + solution)

            story = self.NextVersion.predict(
                story=story, problems=problems,
                solution=solution,
                seriesname=seriesname
            )
        return story

    def MultiGenerate(
            self, seriesname,
            improvementSteps=3,):
        story = self.generateInitialStory(seriesname, True)
        story = self.improve(seriesname, story, improvementSteps)
        print("Generated Story:" + story)
        
        return story