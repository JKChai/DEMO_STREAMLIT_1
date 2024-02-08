import os
import tomli
import pyodbc

class SetupFactory:
    """Setup object for the application
    """
    def __init__(self):
        self.rootpath  = self.__get_root_path()
        self.query, self.cnxn = self.__get_cursor_obj()

    def __get_root_path(self):
        """get full directory path of the running script
        
        Returns:
            str: absolute path of directory 
        """
        fnamepath = os.path.abspath(__file__)
        filepath  = os.path.dirname(fnamepath)

        return filepath

    def __get_config(self):

        fpath = os.path.join(
            self.rootpath,
            "..",
            ".config",
            "config.toml"
            )

        if os.path.isfile(fpath):
            with open(fpath, mode="rb") as f:
                config = tomli.load(f)
        else:
            config = {
                "MSSQLSERVER":{
                    "SERVER":"SERVER",
                    "DATABASE":"DATABASE",
                    "TRUSTEDC":"TRUSTEDC",
                    "SQLQUERY":"SQLQUERY"
                }
            }

        return config

    def __get_cursor_obj(self):
        config   = self.__get_config()
        server   = config["MSSQLSERVER"]["SERVER"]
        database = config["MSSQLSERVER"]["DATABASE"]
        trustedc = config["MSSQLSERVER"]["TRUSTEDC"]
        sqlquery = config["MSSQLSERVER"]["SQLQUERY"]

        connection_string = f'DRIVER={{SQL Server}};'\
                            f'SERVER={server};'\
                            f'DATABASE={database};'\
                            f'Trusted_Connection={trustedc};'
    
        try:
            connection_object = pyodbc.connect(connection_string)
        except pyodbc.Error as e:
            connection_object = connection_string

        return sqlquery, connection_object
            

