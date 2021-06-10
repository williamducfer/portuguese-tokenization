#New content with collaborators:
/^#COLLABORATORS/,/^ID\tFORM\t/d
#Old content without collaborators:
/^#DESCRIPTION/d
/^ID\tFORM\t/d
/^$/d
