# fastapi_with_mongo_db
This API shows how to set up Fast API with mongo db

## To get started

1. Download and install docker desktop

   For windows [Docker](https://docs.docker.com/desktop/install/windows-install/)

   For linux [Docker](https://docs.docker.com/desktop/install/linux-install/)

   For Mac [Docker](https://docs.docker.com/desktop/install/mac-install/)
   
3. create a `.env`file with the following variables
   ```
   MONGO_USERNAME=enter_mongo_db_username
   MONGO_PASSWORD=enter_mongo_db_password
   ME_ADMINUSERNAME=enter_mongo_db_express_username
   ME_ADMINPASSWORD=enter_mongo_db_express_password
   ME_MONGODB_URL=mongodb://username:password@mongo:27017/
   TITLE=enter_your_title_api
   ```
   
   >Replace `username` and `password` in `ME_MONGODB_URL` with your mongo username and mongo password respectively.

3. open command prompt or terminal.

   Run `docker-compose -f docker-compose.dev.yml`
   This will start the containers

4. Open your browser

   Run [http://locahost:8081]()

   This will open mongo express.

   Create a database and a collection inside mongo express
   
5. Run [http://localhost:8000/docs]() to open the interactive swagger UI.
