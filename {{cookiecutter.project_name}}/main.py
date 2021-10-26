# -*- coding: utf-8 -*-

# python core libraries
import logging
import argparse

# 3rd party libraries

# custom libraries

def main() -> None:
	logger = logging.getLogger(__name__)
	logger.debug("a debug message")
	logger.info("a info message")
	logger.warning("a warning message")

if __name__ == '__main__':
	# Initiate argument parser
	parser = argparse.ArgumentParser(prog='face_recognition',)
	parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
	args = parser.parse_args()
	
	# Initiate the logger
	logging.basicConfig(
		filename = 'face_recognition.log', 
		level = logging.DEBUG if args.verbose else logging.INFO, 
		format = '%(asctime)s|%(name)s|%(levelname)s|%(message)s'
	)

	main()