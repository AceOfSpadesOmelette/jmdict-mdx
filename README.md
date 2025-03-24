# jmdict-mdx
A tool to convert JMDict Japanese dictoinary from .json to .txt for building .mdx

# Overview
The dictionary is designed to closely resemble Jisho.org, featuring minimal styling to accommodate both light and dark modes.

Words that can be represented by different kanji, such as うんぬん (云云, 云々), are listed as separate entries. This allows for easier lookup while maintaining the same definitions across variants.

The output is designed with minimal styling for easy reading and navigation.

# Prerequisite
You will need Python 3.7+ in order to run the script.

# Usage
Step 1: Download the script from this repo.

Step 2: Grab the latest release of jmdict-eng-<version>+<time>.json.zip from scriptin's jmdict-simplified repo:

https://github.com/scriptin/jmdict-simplified/releases/tag/3.6.1+20250317122830

Extract the .zip. Move/copy the .json to the folder directory same as the script.

Step 3: Open the .py script. Update the fields of input_file and output_file.

Step 4: Run the script and wait for it to complete.

# What's next?
You should now have a .txt output file sharing the same name as the .json input. This .txt file serves as the dictionary file.

You may want to provide a description for your dictionary using JMDict.info.txt as a reference.

Use an MDX builder like MdxBuilder.exe to compile the dictionary, using the .txt output as the dictionary and JMDict.info.txt as the description. Upon merging, you will create an .mdx file compatible with dictionary apps such as MDict.
