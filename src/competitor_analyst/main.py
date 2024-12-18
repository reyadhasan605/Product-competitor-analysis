#!/usr/bin/env python
import sys
import warnings
from crew import CompetitorAnalyst
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'cars'  ### Write your desired product name
    }
    CompetitorAnalyst().crew().kickoff(inputs=inputs)
run()
