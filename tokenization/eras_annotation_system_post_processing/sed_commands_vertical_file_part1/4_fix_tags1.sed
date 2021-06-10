# Command to fix tags affected by the previous commands. If a tag B-.* is followed by another
# tag B-.*, then changes the second tag to I-.*
/\tB-.*$/{N; s/\(\tB-[^\n]*\n[^\n\t]*\t\)B-\([^\n]*\)/\1I-\2/ }
