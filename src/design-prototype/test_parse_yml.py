import yaml

def test_load_examples():

    with open("example_config.yml") as efile:
        config = yaml.safe_load(efile)
        print(config)

    with open("model_A_2D.yml") as efile:
        config = yaml.safe_load(efile)
        print(config)


if __name__ == "__main__":
    test_load_examples()
