log_config = {
    'version': 1,
    'formatters': {
        'log_formatter': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s %(message)s'
        }
    },
    'handlers': {
        'log_to_stderr': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stderr',
            'formatter': 'log_formatter'
        },
        'log_to_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'DEFAULT_NAME.log',
            'formatter': 'log_formatter',
            'mode': 'w'
        }
    },
    'loggers': {
        'stress_logger': {
            'propagate': False,
            'level': 'DEBUG',
            'handlers': ['log_to_stderr',
                         'log_to_file']
        }
    }
}

tests = {
    'max_batch_size': {
        'test_name': 'max_batch_size',
        'batch_size': list(range(10, 201, 10)),
        'utt_length': 20,
        'infers_num': 1
    },
    'max_string_length_batch_1': {
        'test_name': 'max_string_length_batch_1',
        'batch_size': 1,
        'utt_length': list(range(50, 100, 50)),
        'infers_num': 1
    }
}

test_config = {
  'config_path': 'deployment/ner_chitchat_local/run_config.yaml',
  'dialogs_url': 'https://raw.githubusercontent.com/deepmipt/agent_stress_test/dev/dialogs.txt',
  'infer_timeout': 30,
  'logging': log_config,
  'tests': [tests['max_batch_size'],
            tests['max_string_length_batch_1']]
}