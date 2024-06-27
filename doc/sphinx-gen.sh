cat <<EOT >> ../src/api/conf.py
.. toctree::
   :maxdepth: 2

   main
   db
   routes/secure
EOT

sphinx-build -M html ../src/api .
make html
