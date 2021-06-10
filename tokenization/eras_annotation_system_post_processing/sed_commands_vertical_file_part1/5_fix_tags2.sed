# Command to fix tags affected by the previous commands. If a tag I-.* is followed by a tag B-.*,
# it changes the second tag to I-.*. This process is done recursively
:begin; /\tI-.*$/ {N; s/\(\tI-[^\n]*\n[^\n\t]*\t\)B-\([^\n]*\)/\1I-\2/; bbegin; }
