from configurations.converter import register_converter_configurations
from configurations.data_loader import register_data_loader_configurations
from configurations.evaluation import register_evaluation_configurations
from configurations.models import register_model_configurations
from configurations.processor import register_processor_configurations
from configurations.routine import register_routine_configurations
from configurations.tasks import register_task_configurations
from configurations.tokenizers import register_tokenizer_configurations
from configurations.callbacks import register_callback_configurations
from configurations.calibrators import register_calibrator_configurations

# Import simplified tasks for testing
try:
    from configurations.simplified_tasks import register_simplified_tasks
except ImportError:
    print("Warning: Could not import simplified tasks")

# Data Loader
register_data_loader_configurations()

# Processor
register_processor_configurations()

# Tokenizer
register_tokenizer_configurations()

# Converter
register_converter_configurations()

# Evaluation
register_evaluation_configurations()

# Callbacks
register_callback_configurations()

# Routine
register_routine_configurations()

# Model
register_model_configurations()

# Calibrator
register_calibrator_configurations()

# Task
register_task_configurations()

# Simplified Tasks for Testing
try:
    register_simplified_tasks()
except Exception as e:
    print(f"Warning: Could not register simplified tasks: {str(e)}")
