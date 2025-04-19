# models/job.py

class Task:
    """Base Task class that Job inherits from"""
    def __init__(self):
        self.asset = None
        self.output = {}
        self.score = 0
        self.param = {}

class Job(Task):
    """Job class that handles code generation tasks
    
    This class is used as a template for the AI-generated code.
    It provides a structure for running tasks and calculating scores.
    """

    def __init__(self):
        """Initialize the Job with default values"""
        super().__init__()
        self.param = {
            'max_score': 10  # Default maximum score
        }
        self.output = {
            'detail': [],    # Detailed result from job
            'compact': [],   # Short result from job
            'video': []      # Steps, commands, etc. for doing the job
        }

    def run(self):
        """Run the job and process the asset
        
        This method should be implemented by AI-generated code
        to perform specific tasks based on the prompt.
        """
        asset = self.asset
        
        # Initialize output containers
        self.output['detail'] = []  # Detailed result from job
        self.output['compact'] = []  # Short result from job
        self.output['video'] = []  # Steps, commands, etc. for doing the job
        
        # Implementation will be provided by AI-generated code
        pass

    def calculate_score(self):
        """Calculate a score between 0 and 10 based on job results
        
        Score ranges:
        - score == 1: information
        - 1 < score < 4: low
        - 4 <= score < 7: medium
        - 7 <= score < 9: high
        - 9 <= score < 11: critical
        """
        # Set score to something meaningful based on the job results
        # This will be implemented by AI-generated code
        self.score = self.param['max_score']