from setuptools import setup, find_packages


setup(
    name='jowon',
    version='${version}',
    description='Blog System base on django',
    author='jowon',
    author_email='',
    url='',
    license='MIT',
    # 指明要打入的包, find_packages函数发现指定目录下的所有python包
    packages=find_packages('typeidea'),
    # 指明上面package的包都在哪个目录下，如果在setup.py同级目录则可以不写
    package_dir={'': 'typeidea'},
    # 指明除了.py文件还需要打包哪些文件到最终的安装包里。对应的值需要是字典格式。
    # package_data={
    #     '': ['themes/*/*/*/*', ]
    # },
    # 与package_dir的作用相同，不同需要依赖MANIFEST.ini文件
    include_package_data=True,


    # 指明依赖版本
    install_requires=[
        'django==1.11.29',
        'django_autocomplete_light==3.2.10',
        'django_ckeditor==5.4.0',
        'django-crispy-forms==1.6.1',
        'django-formtools==2.0',
        'django-debug-toolbar==1.9.1',
        'django-import-export==0.6.0',
        'django-js-asset==1.1.0',
        'django-reversion==2.0.1',
        'django-silk==3.0.0',
        'django-simple-captcha==0.5.5',
        'djangorestframework==3.8.2',
        'Fabric3==1.14.post1',
        'mistune==3.0.1',
        'Pillow',
        'PyMySQL==1.1.0',
        'supervisor==4.2.5',

        'coreapi==2.3.3',
        'httplib2==0.9.2',
        'six==1.10.0',
        'gunicorn==19.8.1',
    ],
    # 额外的依赖
    extras_require={
        'ipython': ['ipython==7.6.1']
    },
    # 指明要放到bin目录下的可执行文件，这里把manage.py放进去
    scripts=[
        'typeidea/manage.py',
    ],
    # 表示程序执行的入口点，比较常用的就是console_scripts，用来生成一个可执行文件到bin目录下
    entry_points={
        'console_scripts': [
            'typeidea_manage = manage:main',
        ]
    },
    # 说明项目的当前状况
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.7',
    ],

)
