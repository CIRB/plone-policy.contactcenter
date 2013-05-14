from setuptools import setup, find_packages

version = '1.0.1.dev0'

setup(name='policy.contactcenter',
      version=version,
      description="",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Benoit Suttor',
      author_email='bsuttor@cirb.irisnet.be',
      url='https://github.com/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['policy'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'Products.LinguaPlone',
          'cirb.zopemonitoring',
          # -*- Extra requirements: -*-
          'plonetheme.contactcenter',
          'webcouturier.dropdownmenu',
          'collective.quickupload',
          'Products.PloneFormGen',
          'Solgema.fullcalendar',
          'collective.easyslider',
          'collective.ckeditor',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
