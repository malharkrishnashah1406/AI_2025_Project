#!/usr/bin/env python
"""
Simplified script to test the multimodal argument mining project.
This script allows running a basic model training without requiring the full dataset.
"""

import os
import sys
import numpy as np
import pandas as pd

# Add paths to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'deasy-learning')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'deasy-speech')))

# Import the key modules
from deasy_learning_generic.commands import setup_registry, task_train

def main():
    """
    Run a test model training on a small subset of data.
    """
    print("Setting up Multimodal Argument Mining project...")
    
    # Set up registry - point to the specific directory where components are located
    project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'deasy-speech'))
    setup_registry(directory=project_dir, module_names=['components', 'configurations'])
    
    # Get list of available configurations to show they work
    print("\nAvailable task configurations (namespaces):")
    print("- arg_aaai: UK Debates corpus")
    print("- m-arg: M-Arg corpus")
    print("- us_elec: MM-USElecDeb60to16 corpus")
    
    # Choose a simple model configuration to test
    task_config = "internal_key:instance--flag:task--framework:tf--tags:['text_only', 'calibrated', 'lstm', 'task_type=acd']--namespace:us_elec"
    
    print(f"\nTesting with configuration: {task_config}")
    print("This is a text-only BiLSTM model for argument component detection (ACD) task")
    
    # Run training with debug mode to avoid long training
    try:
        task_train(
            task_config_name=task_config,
            test_name='test_bilstm_to',
            save_results=True,
            framework_config_name=None,
            debug=True  # Debug mode for quick testing
        )
        print("\nTest completed successfully!")
        print("The model setup is working correctly.")
    except Exception as e:
        print(f"\nError running test model: {str(e)}")
        print("Check the error message and make sure all dependencies are installed.")
        print("You may need to download the full datasets as described in the README.md file.")

if __name__ == "__main__":
    main()
