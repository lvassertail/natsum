import os
import argparse


def write_new_format_to_file(orig_file_path, new_file_path, line_length_limit):
  """Reads all the bbids and write them to out file."""
  print("Preprocessing file %s into file %s..." % (orig_file_path, new_file_path))

  new_file = open(new_file_path, "w", encoding="utf8")

  with open(orig_file_path, "r") as orig_file:
    for line in orig_file:
      new_line = " ".join(line.lower().strip().split()[:line_length_limit])

      new_file.write(new_line+"\n")

  new_file.close()
  print("Finished writing file %s"% (new_file_path))


if __name__ == '__main__':

  parser = argparse.ArgumentParser(description='XSum formatting')
  parser.add_argument('--orig_files_dir', type=str)
  parser.add_argument('--finished_files_dir', type=str)
  args = parser.parse_args()

  # Create some new directories
  if not os.path.exists(args.finished_files_dir): os.makedirs(args.finished_files_dir)

  # Read the tokenized stories, do a little postprocessing then write to text files
  write_new_format_to_file(os.path.join(args.orig_files_dir, "test.source"), os.path.join(args.finished_files_dir, "test.document"), 400)
  write_new_format_to_file(os.path.join(args.orig_files_dir, "test.target"), os.path.join(args.finished_files_dir, "test.summary"), 90)
  write_new_format_to_file(os.path.join(args.orig_files_dir, "val.source"), os.path.join(args.finished_files_dir, "validation.document"), 400)
  write_new_format_to_file(os.path.join(args.orig_files_dir, "val.target"), os.path.join(args.finished_files_dir, "validation.summary"), 90)
  write_new_format_to_file(os.path.join(args.orig_files_dir, "train.source"), os.path.join(args.finished_files_dir, "train.document"), 400)
  write_new_format_to_file(os.path.join(args.orig_files_dir, "train.target"), os.path.join(args.finished_files_dir, "train.summary"), 90)
	
