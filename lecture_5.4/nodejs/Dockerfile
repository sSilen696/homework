FROM node



RUN git clone https://github.com/simplicitesoftware/nodejs-demo.git

WORKDIR /nodejs-demo
EXPOSE 3000
RUN sed -i "s/localhost/0.0.0.0/" app.js
RUN npm install


CMD  ["npm", "start"]