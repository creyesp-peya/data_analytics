# Virtual environment
Despite there are many ways to create your own virtual environment,
we recommend using an environment file with the name of the project 
or the user to manage all dependencies and variable. It makes a better 
development workspace. You can use this [environment file](conda_environment/environment.yaml)

```shell
conda env create -f environment.yaml
```

# References
[Advance pip dependencies on env file](https://github.com/conda/conda/blob/54e4a91d0da4d659a67e3097040764d3a2f6aa16/tests/conda_env/support/advanced-pip/environment.yml)
[Pip documentation](https://pip.pypa.io/en/stable/reference/pip_install/)
