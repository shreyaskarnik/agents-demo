from crewai import Task, Crew
from agents import EngineeringCrew
import os

os.environ["OPENAI_API_KEY"] = "sk-asdfg"
agents = EngineeringCrew()
task1 = Task(
    description=f"Find out all the tickets status = Done by the current user in the last {num_weeks} weeks in the {project_key} project. Return results as JSON no other output format.".format(
        num_weeks=4, project_key="MY_PROJECT_KEY"
    ),
    agent=agents.jira_expert(),
)
task2 = Task(
    description="Summarize the work to be done in natural language. You are given a JSON input. Write a status report to be submitted to the manager on what got done in the last 6 weeks. be very thorough, fetch additional details/comments on each issue if needed. Return report as markdown include the links to the tickets. The heading of the report should be the date range.",
    agent=agents.communication_expert(),
)
task3 = Task(
    description="Write a markdown document that can be used as a report to the manager. Use the best layout/formatting for maximum readability. Save it to a file with appropriate name.",
    agent=agents.file_writer(),
)
crew = Crew(
    agents=[
        agents.jira_expert(),
        agents.communication_expert(),
        agents.file_writer(),
    ],
    tasks=[task1, task2, task3],
    verbose=True,
)

result = crew.kickoff()
