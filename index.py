#Video-Dehaing using MRF model
#Written in Python 2.7

#Imports
import argparse
import sys
import video_dehaze as vd

def main(args):

	input_data = args.input
	output = args.out

def parse_arguments(argv):
	
	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type=str, help='Path to the data directory containing input data', default='~/input')
	parser.add_argument('--out', type=str, help='Path to the output directory.', default='~/output')
	
	return parser.parse_args(argv)

if __name__ == '__main__':
	
	main(parse_arguments(sys.argv[1:]))
