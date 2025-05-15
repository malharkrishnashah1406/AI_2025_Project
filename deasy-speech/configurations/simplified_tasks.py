"""
Simplified task configurations for the test model.
"""

from deasy_learning_generic.configuration import TaskConfiguration, ModelParam
from deasy_learning_generic.registry import ComponentFlag, ProjectRegistry, RegistrationInfo

def register_simplified_tasks():
    """
    Register simplified task configurations for testing.
    """
    # Task for text-only LSTM on US Elections dataset (ACD task)
    task_config = TaskConfiguration(
        data_loader_registration_info=RegistrationInfo(
            flag=ComponentFlag.DATA_LOADER,
            framework='generic',
            tags=['text_only', 'task_type=acd'],
            namespace='us_elec',
            internal_key=ProjectRegistry.COMPONENT_KEY
        ),
        routine_registration_info=RegistrationInfo(
            flag=ComponentFlag.ROUTINE,
            framework='tf',
            tags=['default'],
            namespace='default',
            internal_key=ProjectRegistry.COMPONENT_KEY
        ),
        model_registration_info=RegistrationInfo(
            flag=ComponentFlag.MODEL,
            framework='tf',
            tags=['lstm', 'text_only', 'calibrated'],
            namespace='us_elec',
            internal_key=ProjectRegistry.COMPONENT_KEY
        )
    )
    
    # Add task parameters
    task_config.add_param(ModelParam(name='batch_size', value=8, flags=[ComponentFlag.ROUTINE]))
    task_config.add_param(ModelParam(name='epochs', value=2, flags=[ComponentFlag.ROUTINE]))
    task_config.add_param(ModelParam(name='learning_rate', value=0.001, flags=[ComponentFlag.ROUTINE]))
    task_config.add_param(ModelParam(name='evaluation_steps', value=10, flags=[ComponentFlag.ROUTINE]))
    task_config.add_param(ModelParam(name='task_type', value='acd', flags=[ComponentFlag.DATA_LOADER]))
    
    # Register the configuration
    ProjectRegistry.register_configuration(
        configuration=task_config,
        framework='tf',
        namespace='us_elec',
        tags=['text_only', 'calibrated', 'lstm', 'task_type=acd']
    )
    
    # Task for text-audio LSTM on US Elections dataset (ACD task)
    task_config_multimodal = TaskConfiguration(
        data_loader_registration_info=RegistrationInfo(
            flag=ComponentFlag.DATA_LOADER,
            framework='generic',
            tags=['text_audio', 'task_type=acd'],
            namespace='us_elec',
            internal_key=ProjectRegistry.COMPONENT_KEY
        ),
        routine_registration_info=RegistrationInfo(
            flag=ComponentFlag.ROUTINE,
            framework='tf',
            tags=['default'],
            namespace='default',
            internal_key=ProjectRegistry.COMPONENT_KEY
        ),
        model_registration_info=RegistrationInfo(
            flag=ComponentFlag.MODEL,
            framework='tf',
            tags=['lstm', 'text_audio', 'calibrated', 'use_audio_features=False'],
            namespace='us_elec',
            internal_key=ProjectRegistry.COMPONENT_KEY
        )
    )
    
    # Add task parameters
    task_config_multimodal.add_param(ModelParam(name='batch_size', value=8, flags=[ComponentFlag.ROUTINE]))
    task_config_multimodal.add_param(ModelParam(name='epochs', value=2, flags=[ComponentFlag.ROUTINE]))
    task_config_multimodal.add_param(ModelParam(name='learning_rate', value=0.001, flags=[ComponentFlag.ROUTINE]))
    task_config_multimodal.add_param(ModelParam(name='evaluation_steps', value=10, flags=[ComponentFlag.ROUTINE]))
    task_config_multimodal.add_param(ModelParam(name='task_type', value='acd', flags=[ComponentFlag.DATA_LOADER]))
    task_config_multimodal.add_param(ModelParam(name='use_audio_features', value=False, flags=[ComponentFlag.DATA_LOADER]))
    
    # Register the configuration
    ProjectRegistry.register_configuration(
        configuration=task_config_multimodal,
        framework='tf',
        namespace='us_elec',
        tags=['text_audio', 'calibrated', 'lstm', 'task_type=acd', 'use_audio_features=False']
    )
