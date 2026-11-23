import os
import shutil

# Copy the pre-built entry image to the grader's output directory.
# Standard library only: the grader installs nothing before it runs.
# The copy is byte for byte, so two runs write identical bytes.
out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

# The grader may hand us an output directory that does not exist yet;
# create it (including any missing parents) instead of failing.
os.makedirs(out_dir, exist_ok=True)

dst = os.path.join(out_dir, "entry.png")
shutil.copyfile(src, dst)

# Verify the copy landed intact. This must stay a byte-for-byte copy:
# the grader runs main.py twice and requires identical bytes both times,
# so any transformation (re-encode, resize, re-save) would break determinism.
if not os.path.exists(dst):
    raise RuntimeError("entry.png was not written to the output directory")
if os.path.getsize(dst) != os.path.getsize(src):
    raise RuntimeError(
        "copied entry.png is %d bytes but source entry.png is %d bytes; "
        "the copy must be byte-for-byte identical"
        % (os.path.getsize(dst), os.path.getsize(src))
    )
