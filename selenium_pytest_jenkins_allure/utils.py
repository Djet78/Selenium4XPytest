import os


def add_pytest_res_evn_file(pytest_config, key, value):
    alluredir = pytest_config.getoption('--alluredir')
    if not os.path.exists(alluredir):
        os.mkdir(alluredir)

    env_data = f'{key.upper()}={value}\n'

    allure_env_path = os.path.join(alluredir, 'environment.properties')
    if not os.path.exists(allure_env_path):
        with open(allure_env_path, 'w') as _f:
            _f.write(env_data)
    else:
        with open(allure_env_path, 'a') as _f:
            _f.write(env_data)


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance
