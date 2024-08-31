#!/usr/bin/env python
import sys,os
from match_to_proposal.crew import MatchToProposalCrew

os.environ["OPENAI_API_KEY"]="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"
os.environ['OPENAI_MODEL_NAME']= "llama-3.1-70b-versatile"
os.environ['OPENAI_API_BASE']="https://api.groq.com/openai/v1"

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'path_to_jobs_csv': 'src/match_to_proposal/data/jobs.csv',
        #'path_to_cv' : 'src\\match_to_proposal\\data\\CV'
        'path_to_cv' :  'src/match_to_proposal/data/cv.md',
        'path_to_cv2':  'src/match_to_proposal/data/cv2.md',
        'path_to_cv3':  'src/match_to_proposal/data/cv3.md',
        'path_to_cv4':  'src/match_to_proposal/data/cv4.md',
        'path_to_cv5':  'src/match_to_proposal/data/cv5.md'

    }
    MatchToProposalCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'path_to_jobs_csv': 'src/match_to_proposal/data/jobs.csv',
        #'path_to_cv' : 'src\\match_to_proposal\\data\\CV'
        'path_to_cv' :  'src/match_to_proposal/data/cv.md',
        'path_to_cv2':  'src/match_to_proposal/data/cv2.md',
        'path_to_cv3':  'src/match_to_proposal/data/cv3.md',
        'path_to_cv4':  'src/match_to_proposal/data/cv4.md',
        'path_to_cv5':  'src/match_to_proposal/data/cv5.md'

    }
    try:
        MatchToProposalCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
