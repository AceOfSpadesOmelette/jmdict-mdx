# jmdict-mdx
A tool to convert JMDict Japanese dictoinary from .json to .txt for building .mdx

The dictionary is designed to resemble Jisho.org as close as possible. It features minimal styling (no text styling, unique bordering on example sentences, etc.) to support both light and dark modes of a device. 

Words that can be rewritten as different kanjis to convey different meanings will be separated as different entries for better lookup. For instance, うんぬん has two kanji variants, 云云 and 云々, but they all share the same definition and you will be able to look for any word in the dictionary. 

# Prerequisite
You will need Python 3.7+ in order to run the script.

# Usage
Step 1: Download the script from this repo.

Step 2: Grab the latest release of jmdict-eng-<version>+<time>.json.zip from scriptin's jmdict-simplified repo:
https://github.com/scriptin/jmdict-simplified/releases/tag/3.6.1+20250317122830

Step 3: Open the .py script. Update the fields of input_file and output_file.

Step 4: Run the script and wait for it to complete.

# What's next?
You should have a .txt output sharing the same name as the .json input. This .txt file is the dictionary file.

You may want to provide the description which you can use JMDict.info.txt as reference.

Get an MDX builder like MdxBuilder.exe to build the dictionary, with said .txt output as the dictionary and JMDict.info.txt as the description. Upon merging, you will get an .mdx file which is compatible to dictionary apps such as MDict.
