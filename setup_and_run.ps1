# PowerShell script to set up and run the Multimodal Argument Mining project
# This script handles the setup and test execution for the project

Write-Host "=========================================================="
Write-Host "  Multimodal Argument Mining Project Setup and Test Script"
Write-Host "=========================================================="
Write-Host ""

# Step 1: Create necessary directories if they don't exist
Write-Host "Step 1: Setting up directory structure..."
$directories = @(
    "data\arg_aaai",
    "data\m-arg",
    "data\us_elec",
    "data\us_elec\audio_clips",
    "data\m-arg\audio_samples"
)

foreach ($dir in $directories) {
    $path = Join-Path -Path (Get-Location) -ChildPath $dir
    if (-not (Test-Path -Path $path)) {
        New-Item -Path $path -ItemType Directory -Force
        Write-Host "  Created directory: $dir"
    } else {
        Write-Host "  Directory already exists: $dir"
    }
}

# Step 2: Install or verify dependencies
Write-Host ""
Write-Host "Step 2: Verifying and installing Python dependencies..."
Write-Host "  Installing core requirements..."
pip install dill gensim nltk scikit-learn scipy simplejson tqdm

Write-Host "  Installing TensorFlow and related packages..."
pip install tensorflow tf-keras huggingface-hub tensorflow-addons transformers

Write-Host "  Installing audio processing packages..."
pip install resampy pydub

# Step 3: List tasks to verify configuration
Write-Host ""
Write-Host "Step 3: Verifying project configuration..."
Write-Host "  Running list_tasks.py to verify configuration..."
python deasy-speech/runnables/list_tasks.py

# Step 4: Run the test model script
Write-Host ""
Write-Host "Step 4: Running test model..."
Write-Host "  This will attempt to train a simple model on the sample data..."
Write-Host "  Note: This may show errors if all dependencies are not properly installed."
python run_test_model.py

Write-Host ""
Write-Host "=========================================================="
Write-Host "Setup and test complete!"
Write-Host ""
Write-Host "Next steps for full project setup:"
Write-Host "1. Download full datasets as mentioned in README.md:"
Write-Host "   - UKDebates (arg_aaai2016): http://argumentationmining.disi.unibo.it/aaai2016.html"
Write-Host "   - M-Arg: https://github.com/rafamestre/m-arg_multimodal-argumentation-dataset"
Write-Host "   - Run audio_pipeline.py to generate the MM-USElecDeb60to16 dataset"
Write-Host ""
Write-Host "2. For running full experiments, use the following commands:"
Write-Host "   python deasy-speech/runnables/task_train.py with appropriate parameters"
Write-Host "   python deasy-speech/runnables/task_forward.py for inference"
Write-Host "=========================================================="
 
