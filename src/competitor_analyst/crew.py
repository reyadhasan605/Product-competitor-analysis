from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool, WebsiteSearchTool,SerperDevTool
from dotenv import load_dotenv
from typing import List, Dict
import pandas as pd
load_dotenv()


@CrewBase
class CompetitorAnalyst():
	"""CompetitorAnalyst crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	ollama_llm = LLM(
		model='ollama/llama3.2:3b',
		base_url='http://localhost:11434',
	)



	@agent
	def Data_retrieval(self) -> Agent:
		return Agent(
			config=self.agents_config['data_retrieval'],
			verbose=True,
			llm = self.ollama_llm,
			tools =[SerperDevTool(),
					ScrapeWebsiteTool(),
					WebsiteSearchTool(website='https://www.linkedin.com/'),
					WebsiteSearchTool(website='https://www.reddit.com/'),
					WebsiteSearchTool('https://www.g2.com/')]
		)

	@agent
	def NLP_processing(self) -> Agent:
		return Agent(
			config=self.agents_config['nlp_processing'],
			verbose=True,
			llm = self.ollama_llm,
		)

	@agent
	def Feature_comparison(self) -> Agent:
		return Agent(
			config=self.agents_config['feature_comparison'],
			verbose=True,
			llm = self.ollama_llm,
		)

	@agent
	def SWOT_analysis(self) -> Agent:
		return Agent(
			config=self.agents_config['swot_analysis'],
			verbose=True,
			llm = self.ollama_llm,
		)

	@agent
	def Report_generation(self) -> Agent:
		return Agent(
			config=self.agents_config['report_generation'],
			verbose=True,
			llm = self.ollama_llm
		)


############# task ################

	@task
	def Data_retrieval_task(self) -> Task:
		return Task(
			config=self.tasks_config['data_retrieval_task'],
		)

	@task
	def NLP_processing_task(self) -> Task:
		return Task(
			config=self.tasks_config['nlp_processing_task'],
			output_file='processing.md'
		)
	@task
	def Feature_comparison_task(self) -> Task:
		return Task(
			config=self.tasks_config['feature_comparison_task'],
			output_file='feature.md'
		)
	@task
	def SWOT_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['swot_analysis_task'],
			output_file='swot.md'
		)

	@task
	def Report_generation_task(self) -> Task:
		return Task(
			config=self.tasks_config['report_generation_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CompetitorAnalyst crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)
