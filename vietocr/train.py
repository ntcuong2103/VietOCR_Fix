import argparse

from vietocr.model.trainer import Trainer
from vietocr.tool.config import Cfg

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', required=True, default='config/base.yml', help='see example at ')
    # parser.add_argument('--checkpoint', required=False, help='your checkpoint')
    
    args = parser.parse_args()
    config = Cfg.load_config_from_file(args.config)

    trainer = Trainer(config)

    if config['trainer']['checkpoint']:
        trainer.load_weights(config['trainer']['checkpoint'])
        
    # trainer.train()
    ret = trainer.predict()
    pass

if __name__ == '__main__':
    main()