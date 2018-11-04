# %%
import os
import re


# %%
def replace(f_input, f_output):
    with open(f_input, encoding='utf-8', mode='rt') as f:
        t = f.read()
        t = re.sub(r'^## ', '### ', t, flags=re.M)
        t = re.sub(r'^# ', '## ', t, flags=re.M)
        with open(f_output, encoding='utf-8', mode='wt') as f_w:
            f_w.write(t)


# %%
if __name__ == '__main__':
    file_list = os.listdir('input')
    for file_sample in file_list:
        f_input = os.path.join('input', file_sample)
        f_output = os.path.join('output', file_sample)
        replace(f_input, f_output)
