import os
import shutil

tomo_ref = "/Users/vikashrungta/code/tomo/reference"
delta_content = "/Users/vikashrungta/code/delta/content"

mapping = {
    "amivora/posts": "blogs/amivora.substack.com",
    "aparnacd/posts": "blogs/aparnacd.substack.com",
    "debliu/posts": "blogs/debliu.substack.com",
    "lg/posts": "blogs/lg.substack.com",
    "boz": "blogs/boz",
    "gibsonbiddle": "blogs/gibsonbiddle",
    "articles": "articles",
    "books": "books",
    "memos": "memos",
    "videos_and_podcasts": "videos_and_podcasts"
}

for src_rel, dst_rel in mapping.items():
    src_dir = os.path.join(tomo_ref, src_rel)
    dst_dir = os.path.join(delta_content, dst_rel)
    
    if not os.path.exists(src_dir):
        print(f"Source {src_dir} does not exist, skipping.")
        continue
        
    os.makedirs(dst_dir, exist_ok=True)
    
    # deduplicate and copy files
    for root, dirs, files in os.walk(src_dir):
        for f in files:
            if f == ".DS_Store": continue
            src_file = os.path.join(root, f)
            rel_path = os.path.relpath(src_file, src_dir)
            dst_file = os.path.join(dst_dir, rel_path)
            
            os.makedirs(os.path.dirname(dst_file), exist_ok=True)
            
            if os.path.exists(dst_file):
                print(f"Skipping existing file (dedup): {dst_file}")
                # Remove from source if already exists in target (dedup)
                if os.path.exists(src_file):
                    os.remove(src_file)
            else:
                print(f"Moving {src_file} -> {dst_file}")
                shutil.copy2(src_file, dst_file)
                # Remove from source after successful move
                if os.path.exists(src_file):
                    os.remove(src_file)

# Cleanup sources
for src_rel in mapping.keys():
    top_dir = src_rel.split("/")[0]
    p = os.path.join(tomo_ref, top_dir)
    if os.path.exists(p):
        print(f"Removing source dir {p}")
        shutil.rmtree(p)

print("Done")
