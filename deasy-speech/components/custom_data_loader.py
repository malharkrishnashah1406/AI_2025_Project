"""
Custom data loader for handling the sample datasets created for testing.
This ensures we can run the project without having the complete datasets.
"""

import os
import json
import pandas as pd
import numpy as np
from deasy_learning_generic.data import DataInstance, FeatureType, LabelType, DataLoader

class SampleDataLoader(DataLoader):
    """
    A simple data loader for the sample datasets we've created.
    """

    def __init__(self, data_path, dataset_type="us_elec"):
        """
        Initialize the sample data loader.
        
        Args:
            data_path: Path to the sample dataset file
            dataset_type: Type of dataset ('arg_aaai', 'm-arg', or 'us_elec')
        """
        self.data_path = data_path
        self.dataset_type = dataset_type
        self.data = None
        self.load_data()
        
    def load_data(self):
        """
        Load the sample dataset based on its type.
        """
        if self.dataset_type in ['arg_aaai', 'm-arg']:
            with open(self.data_path, 'r') as f:
                self.data = json.load(f)
        elif self.dataset_type == 'us_elec':
            self.data = pd.read_csv(self.data_path)
        else:
            raise ValueError(f"Unknown dataset type: {self.dataset_type}")
            
    def get_samples(self):
        """
        Convert the sample data into DataInstance objects.
        """
        samples = []
        
        if self.dataset_type in ['arg_aaai', 'm-arg']:
            # JSON format datasets
            for item in self.data['samples']:
                features = {
                    'text': FeatureType(item['text'], 'text')
                }
                
                # Add audio feature for m-arg dataset
                if self.dataset_type == 'm-arg' and 'audio_path' in item:
                    features['audio'] = FeatureType(item['audio_path'], 'audio')
                    
                labels = {
                    'argument_type': LabelType(item['label'], is_categorical=True)
                }
                
                samples.append(DataInstance(features=features, labels=labels))
                
        elif self.dataset_type == 'us_elec':
            # CSV format for US elections dataset
            for _, row in self.data.iterrows():
                features = {
                    'text': FeatureType(row['Speech'], 'text')
                }
                
                # Add audio feature if available
                if 'idClip' in row and row['idClip'] is not None:
                    features['audio'] = FeatureType(row['idClip'], 'audio')
                    
                # Labels based on the dataset structure
                labels = {}
                if 'Component' in row:
                    labels['component'] = LabelType(row['Component'], is_categorical=True)
                if 'ArgumentativeType' in row:
                    labels['arg_type'] = LabelType(row['ArgumentativeType'], is_categorical=True)
                
                samples.append(DataInstance(features=features, labels=labels))
                
        return samples
        
    def get_train_test_split(self, test_ratio=0.2, random_seed=42):
        """
        Split the sample data into training and test sets.
        """
        samples = self.get_samples()
        np.random.seed(random_seed)
        indices = np.random.permutation(len(samples))
        test_size = int(len(samples) * test_ratio)
        test_indices = indices[:test_size]
        train_indices = indices[test_size:]
        
        train_samples = [samples[i] for i in train_indices]
        test_samples = [samples[i] for i in test_indices]
        
        return train_samples, test_samples
 
