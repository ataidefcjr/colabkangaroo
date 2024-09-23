start = int('4000000000000000000000000000000000', 16)
end = int('7fffffffffffffffffffffffffffffffff', 16)

total_parts = 512
step = (end - start) // total_parts

for part in range(total_parts):
    part_start = start + (step * part)
    if part == total_parts - 1:
        part_end = end  
    else:
        part_end = start + (step * (part + 1)) - 1

    filename = f"ranges/135-{part + 1}.txt"

    with open(filename, 'w') as f:
        f.write(f"{hex(part_start)[2:]}\n")
        f.write(f"{hex(part_end)[2:]}\n")
        f.write("02145d2611c823a396ef6712ce0f712f09b9b4f3135e3e0aa3230fb9b6d08d1e16")

print("Arquivos gerados com sucesso!")
