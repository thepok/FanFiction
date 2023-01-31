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


    def generateInitial(self, seriesname, UseCache=True):
        print("Generating a new FanFiction")
        self.llm.cache=UseCache
        plot = self.initialPlotGenerator.predict(seriesname=seriesname)
        print("Generated Plot: " + plot)
        
        return plot

    def improve(self, seriesname, plot):
        problems = self.problemGenerator.predict(
            plot=plot,
            seriesname=seriesname)
        print("Generated Problems:" + problems)

        solution = self.ProblemFixer.predict(
            plot=plot, seriesname=seriesname, problems=problems
        )
        print("Generated Solution: " + solution)

        nextVersion = self.NextVersion.predict(
            plot=plot, problems=problems,
            solution=solution,
            seriesname=seriesname
        )
        
        return nextVersion
