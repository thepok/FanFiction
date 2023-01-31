from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.cache import SQLiteCache
import langchain


class FanFictionGenerator:
    def __init__(self):
        langchain.llm_cache = SQLiteCache(".langchain.db")

        self.llm = OpenAI(max_tokens=-1, temperature=0.7)
        self.initialPlotGenerator = LLMChain.from_string(
            self.llm, "Write a detailed Story for an new Episode of {seriesname}"
        )

        self.problemGenerator = LLMChain.from_string(
            self.llm,
            """Between >>> and <<< is a new Story for {seriesname}

>>>
{plot}
<<<

Where is the story unclear, where is not detailed enough?

Missing Details:""",
        )

        self.ProblemFixer = LLMChain.from_string(
            self.llm,
            """Between >>> and <<< is a new Story for {seriesname}
>>>
{plot}
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
{plot}
<<< 
The Critics found the following problems:
{problems}

The Authors found this Solution:
{solution}

Now Rewrite the Story with the new Details from the Solution.

New Version:""",
        )

        self.StoryMerger = LLMChain.from_string(self.llm, """Two stories for {seriesname} have to be merged.
Story 1:{plot1}

Story 2:{plot2}

Your task is it to merge this two stories into one more exciting story.

Merged Story:""")

    def merge(self, seriesname, plot1, plot2):
        print("Merging two Stories")
        merged = self.StoryMerger.predict(
            seriesname=seriesname, plot1=plot1, plot2=plot2)
        print("Merged Plot: " + merged)
        return merged

    def generateInitial(self, seriesname, UseCache=True):
        print("Generating a new FanFiction")
        self.llm.cache = UseCache
        plot = self.initialPlotGenerator.predict(seriesname=seriesname)
        print("Generated Plot: " + plot)
        
        return plot

    def improve(self, seriesname, plot, count=1):

        for i in range(count):
            problems = self.problemGenerator.predict(
                plot=plot,
                seriesname=seriesname)
            print("Generated Problems:" + problems)

            solution = self.ProblemFixer.predict(
                plot=plot, seriesname=seriesname, problems=problems
            )
            print("Generated Solution: " + solution)

            plot = self.NextVersion.predict(
                plot=plot, problems=problems,
                solution=solution,
                seriesname=seriesname
            )
        return plot

    def MultiGenerate(
            self, seriesname,
            improvementSteps=3,
            storyCount=2,
            finalImprovementSteps=3):
        plots = []
        for i in range(storyCount):
            plot = self.generateInitial(seriesname, False)
            plot = self.improve(seriesname, plot, improvementSteps)
            print("Generated Plot" + str(i) + ": " + plot)
            plots.append(plot)
        
        mergedPlot = plots[0]
        for i in range(1, len(plots)):
            mergedPlot = self.merge(seriesname, mergedPlot, plots[i])

        # finalImprovement
        mergedPlot = self.improve(
            seriesname, mergedPlot, finalImprovementSteps)
        
        return mergedPlot