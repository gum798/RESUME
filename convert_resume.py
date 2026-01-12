import markdown
import os

def convert_md_to_html(input_file, output_file):
    # Read Markdown content
    with open(input_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert to HTML
    html_content = markdown.markdown(md_content)

    # HTML Template with CSS styling
    html_template = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>서정화 - 이력서</title>
    <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
    <style>
        :root {{
            --primary-color: #2c3e50;
            --accent-color: #34495e;
            --link-color: #2980b9;
            --text-color: #333;
            --bg-color: #f0f2f5;
            --paper-color: #ffffff;
            --border-color: #eee;
        }}
        body {{
            font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif;
            line-height: 1.65;
            color: var(--text-color);
            background-color: var(--bg-color);
            margin: 0;
            padding: 40px 20px;
        }}
        .container {{
            background-color: var(--paper-color);
            max_width: 900px;
            margin: 0 auto;
            padding: 60px 80px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.05);
            border-radius: 4px;
        }}
        
        /* Header & Profile Image */
        h1 {{
            font-size: 2.2rem;
            color: var(--primary-color);
            margin-bottom: 0.5rem;
            letter-spacing: -0.02em;
            border: none;
            padding: 0;
        }}
        /* Profile Image Styling */
        img[alt="Profile"] {{
            width: 180px;
            height: 220px;
            object-fit: cover;
            border-radius: 8px;
            float: right;
            margin-left: 40px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }}
        
        /* Typography & Layout */
        h2 {{
            color: var(--accent-color);
            border-bottom: 2px solid #3498db;
            border-left: none; /* Removed side border */
            padding-bottom: 10px;
            padding-left: 0;
            margin-top: 50px;
            margin-bottom: 20px;
            font-weight: 700;
            font-size: 1.4rem;
        }}
        h3 {{
            color: var(--link-color);
            margin-top: 30px;
            margin-bottom: 12px;
            font-size: 1.15rem;
            font-weight: 600;
        }}
        h4 {{
            color: var(--primary-color);
            font-weight: 600;
            margin-top: 20px;
            margin-bottom: 8px;
        }}
        p {{
            margin-bottom: 1rem;
        }}
        a {{
            color: var(--link-color);
            text-decoration: none;
            font-weight: 500;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        hr {{
            border: 0;
            border-top: 1px solid var(--border-color);
            margin: 40px 0;
        }}

        /* Lists */
        ul {{
            padding-left: 20px;
            margin-top: 0;
        }}
        li {{
            margin-bottom: 6px;
        }}

        /* Code/Badges */
        code {{
            background-color: #f1f3f5;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: monospace;
            color: #c92a2a;
            font-size: 0.9em;
        }}
        
        /* Skills Badge Style */
        h3 + ul {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            padding: 0;
            list-style: none;
            margin-bottom: 25px;
        }}
        h3 + ul li {{
            background-color: #f8f9fa;
            border: 1px solid #e9ecef;
            padding: 4px 12px;
            border-radius: 20px;
            color: #495057;
            font-size: 0.9rem;
            font-weight: 500;
            margin: 0;
        }}
        h3 + ul li strong {{
            color: #212529;
            font-weight: 600;
        }}

        /* Blockquote */
        blockquote {{
            border-left: 4px solid #3498db;
            background-color: #f8f9fa;
            margin: 30px 0;
            padding: 20px;
            color: #555;
            font-style: italic;
            border-radius: 0 4px 4px 0;
        }}

        /* Mobile adjustments */
        @media (max-width: 600px) {{
            body {{
                padding: 0;
                background-color: #fff;
            }}
            .container {{
                padding: 25px;
                box-shadow: none;
            }}
            img[alt="Profile"] {{
                float: none;
                display: block;
                margin: 0 auto 20px;
                width: 100px;
                height: 125px;
            }}
            h1 {{
                text-align: center;
                font-size: 1.8rem;
            }}
            .header-contact {{
                font-size: 0.9rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        {html_content}
    </div>
</body>
</html>
"""

    # Write HTML file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    print(f"Successfully converted {input_file} to {output_file}")

if __name__ == "__main__":
    input_md = "RESUME.md"
    output_html = "index.html"
    
    if os.path.exists(input_md):
        convert_md_to_html(input_md, output_html)
    else:
        print(f"Error: {input_md} not found!")
