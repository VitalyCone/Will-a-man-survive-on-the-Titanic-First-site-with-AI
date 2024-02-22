# Will-a-man-survive-on-the-Titanic-First-site-with-AI

Using AI, the site will show the survival rate of a certain person on the Titanic/
Используя искусственный интеллект, сайт покажет процент выживаемости выбранного человка на Титанике

Required Libraries/Необходимые библиотеки:
pip install flask
pip install keras
pip install pandas
pip install numpy
pip install matplotlib (If you want to train the model 'train_model.py' independently)

For VSCode download Live Server (or similar), the site runs on the server/
Для VSCode скачать расширение Live server(or similar), сайт запускается с локального сервера


Launch/Запуск:
First, run index.html using Live Server, then run the server.py file, check that the server.py port matches the Live Server port

Для начала, запустите index.html с помощью Live Server, потом запустить файл server.py, проверьте чтобы порт server.py совпадал с портом Live Server

  if __name__ == '__main__':
      app.run(debug=True,       ->  port=5501  <-      )
