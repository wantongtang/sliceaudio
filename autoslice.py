#auto slice all file in dir specified in --in_dir

from SliceAudio import slice_audio
import os
import argparse

# parse command line input

PARSER = argparse.ArgumentParser(description = """
								auto slice all file in directory 

								"""								
								)
PAESER.add_argument('-i',
					"in_dir",
					help = "input directory",
					type = "str",
					default = "./")
PARSER.add_argument("")

