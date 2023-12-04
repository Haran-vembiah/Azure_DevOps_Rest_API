
[[_TOC_]]

---
# Sphinx Documentation basic setup

You can create a documentation for code that you maintain in the repository.

## Sphinx initial setup
- Install Sphinx by running the command pip install sphinx in your terminal or command prompt.
- Open a terminal or command prompt and navigate to the directory where you want to create your Sphinx documentation.
- Run the command sphinx-quickstart. This command will walk you through the process of setting up a new Sphinx documentation project.
- Respond to prompt by the sphinx-quickstart command, such as the project name, version, author name, and release date.
- After configuring with the prompt, the sphinx-quickstart command will generate a basic Sphinx documentation structure in the directory that you specified.
- Add your Python modules to the "source" directory. Sphinx will automatically generate documentation for these modules based on their docstrings.

      import os
      import sys
      sys.path.insert(0, os.path.abspath('../..'))

- Open the "conf.py" file in a text editor configure the settings:
  - Add the parent directory of your Sphinx documentation to the Python path, so that Sphinx can find your Python modules.
  - Configure Sphinx to use the autodoc extension for documentation like below:
  
        extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode','sphinx_markdown_builder']
         
    - This will enable the autodoc extension, which will automatically generate documentation for your Python modules based on their docstrings.
  - Open the "index.rst" file in the "source" directory and add the modules to create documentation using autodoc extensions like:
       
        .. automodule:: module 1
            :members:

        .. automodule:: module 2
            :members:


- Build your Sphinx documentation by running the command make html in the command prompt or terminal from the directory where the "Makefile" resides.

- Generate intermediate files (.rst) file, later used as source to generate markdown files to make available on the Azure code wiki for each package available in the repository. Use the below command from the project root.
  -   Excluding tests package which has only the unit test stuffs.
  
          mt-anachem-ta> sphinx-apidoc -o .\doc\source .\ "*test*"
- You can also build an HTML version of your Sphinx documentation using the sphinx-build command, run the command

          mt-anachem-ta> sphinx-build -b html .\doc\source .\doc\build

  - View your Sphinx documentation by opening the "index.html" file in the "doc\build" directory in a web browser.

- You can also generate markdown files for each modules by taking rst files generated already and available in the path doc\source, run the command
  
  - The sphinx extension "sphinx-markdown-builder" should be installed added in the extensions parameter as "sphinx_markdown_builder". 
             mt-anachem-ta> sphinx-build -M markdown .\doc\source .\doc\build
      - Markdown files will be generated under the directory doc\build\markdown
 