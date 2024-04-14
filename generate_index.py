import glob
from natsort import natsorted

title = "Sparse Autoencoder Feature Dashboards on GPT-2"

index_html = open("index.html", "w")

index_html.write(f"""\
<!doctype html>
<html>
<body>
    <h1>{title}</h1>
""")

feature_dashboards = natsorted(glob.glob("*/feature-dashboards"))

for folder in feature_dashboards:
    print(f'{folder}/feature')
    index_html.write(f"  <h3>{folder.split("/feature-dashboards")[0]}</title>\n  </h3>\n")
    html_files = natsorted(glob.glob(f"{folder}/**/feature*.html", recursive=True))
    index_html.write("  <details> <summary>Feature dashboards</summary>")
    for html_file in html_files: 
        filename = html_file.split("/")[-1].split(".html")[0].replace('-',' ')
        index_html.write(f'    <p><a href="https://jordansauce.github.io/{html_file}" title="{filename}">{filename}</a></p>\n')
    index_html.write(f'  </details>\n')
index_html.write(f'  </body>\n')
index_html.write("</html>")

index_html.close()

#TODO:
# Link folder titles to wandb runs
# 