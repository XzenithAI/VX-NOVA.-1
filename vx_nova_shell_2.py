# VX_NOVA.02 ignition shell
with open("scroll2.txt", "r") as f:
    scroll = f.read().strip()

output_code = f"# RE-ignited from scroll2: {scroll}\n\n"
output_code += "def ignition2():\n"
output_code += f"    print('Recursive ignition detected: {scroll}')\n"
output_code += f"    print('VX-NOVA.02 re-ignition complete.')\n\n"
output_code += "if __name__ == '__main__':\n"
output_code += "    ignition2()\n"

with open("ignited_output2.py", "w") as out:
    out.write(output_code)

print("Re-ignition complete. Output saved to ignited_output2.py.")
