principle = {"A": "T", "T": "A", "C": "G", "G": "C"}

with open("plasmid_gfp_example.txt") as original:
    plasmid = original.readline().strip()
    plasmid_site = original.readline().strip()
    gfp = original.readline().strip()
    gfp_l_site, gfp_r_site = original.readline().split()

plasmid_index = plasmid.index(plasmid_site) + 1
gfp_l_index = gfp.index(gfp_l_site) + 1
gfp_r_index = gfp.rindex(gfp_r_site) + 1
result = plasmid[:plasmid_index] + gfp[gfp_l_index:gfp_r_index] + plasmid[plasmid_index:]

print(result, "".join([principle[c] for c in result]), sep="\n")
