# Multimodal Argument Mining Project Setup Guide

This guide provides comprehensive instructions for setting up and running the Multimodal Argument Mining project.

## Project Overview

This project focuses on multimodal argument mining in political debates, analyzing both text and audio to detect and classify argumentative components.

The project consists of three main components:
1. **deasy-learning**: A Python library for performing deep learning experiments
2. **deasy-speech**: The code for the experiments described in the paper
3. **multimodal-dataset**: Code to reproduce the MM-USElecDeb60to16 dataset

## Environment Setup

### Dependencies Installation

This project requires specific versions of libraries. Create a virtual environment and install:

```bash
# Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install core dependencies
pip install dill==0.3.3 gensim==4.0.1 nltk==3.5 numpy==1.18.5 scikit-learn==0.24.0 scipy==1.4.1 simplejson==3.17.2 tqdm==4.56.0

# Install TensorFlow dependencies
pip install huggingface-hub==0.0.8 Keras==2.4.3 Keras-Preprocessing==1.1.2 tensorflow-addons==0.11.2 tensorflow-gpu==2.3.0 tensorflow-probability==0.11.1 tokenizers==0.10.2 transformers==4.6.1

# Install audio processing libraries
pip install pydub resampy
```

### Dataset Preparation

The project requires three datasets:

1. **UKDebates (arg_aaai2016)**
   - Download from: http://argumentationmining.disi.unibo.it/aaai2016.html
   - Place in: `data/arg_aaai/`

2. **M-Arg**
   - Download from: https://github.com/rafamestre/m-arg_multimodal-argumentation-dataset
   - Place in: `data/m-arg/`

3. **MM-USElecDeb60to16**
   - Generate using code in the `multimodal-dataset` folder
   - Run: `python multimodal-dataset/audio_pipeline.py`
   - This will:
     - Download debate videos from YouTube
     - Extract and trim audio files
     - Generate audio chunks
     - Create aligned audio clips
   - *Note: This process can take several hours*
   - Final dataset location: `multimodal-dataset/files/MM-USElecDeb60to16/`

## Directory Structure

Ensure your project has the following directory structure:

```
multimodal-am/
├── deasy-learning/
├── deasy-speech/
├── multimodal-dataset/
├── data/
│   ├── arg_aaai/
│   ├── m-arg/
│   └── us_elec/
└── log/
```

## Running Experiments

### 1. List Available Tasks

To verify the project's configuration and see available tasks:

```bash
python deasy-speech/runnables/list_tasks.py
```

### 2. Training a Model

For example, to train a BiLSTM model with text-only input on the M-Arg dataset:

```bash
python deasy-speech/runnables/task_train.py
```

With the following parameters:
- `task_config_name`: "internal_key:instance--flag:task--framework:tf--tags:['calibrated', 'lstm', 'text_only']--namespace:m-arg"
- `test_name`: "bilstm_to"
- `save_results`: True
- `debug`: False

### 3. Running Inference (Ablation Study)

```bash
python deasy-speech/runnables/task_forward.py
```

With parameters as documented in the main README.md.

## Troubleshooting

### Version Compatibility Issues

This project was developed with specific library versions. If you encounter compatibility issues:

1. Use the exact versions specified in the requirements files
2. Create a clean virtual environment to avoid conflicts
3. For TensorFlow issues with newer Keras versions, install tf-keras: `pip install tf-keras`

### Dataset Issues

If you encounter issues with the dataset generation:

1. Check the manual download links for UKDebates and M-Arg
2. For MM-USElecDeb60to16, you can run the generation process in stages:
   - Download a few specific debates using the `debug.csv` instead of full `dictionary.csv`
   - Use the already generated sample data in `data/us_elec/sample_data.csv`

## Additional Resources

- Original paper: "Multimodal Argument Mining: A Case Study in Political Debates"
- Authors: Eleonora Mancini, Federico Ruggeri, Andrea Galassi, and Paolo Torroni
- Paper link: https://aclanthology.org/2022.argmining-1.15
 
