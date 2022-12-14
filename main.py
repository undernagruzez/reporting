from report_generator.station_data_generator import StationDataGenerator
from src.reporting_config.config import Config
from src.report_generator.summary_data_generator import SummaryDataGenerator

if __name__ == '__main__':
    config = Config('./config/config.properties')
    # SummaryDataGenerator(config, 'summary', 'md').generate_report()
    StationDataGenerator(config, 'version', 'md').generate_report()
