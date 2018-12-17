
use 5gk8s_db

CREATE TABLE TX_HIST (
    id          bigint(20) NOT NULL AUTO_INCREMENT,
    method      varchar(15) NOT NULL,
    resource    varchar(300) NOT NULL,
    remote_addr varchar(150),
    agent       varchar(300),
    data        varchar(2000),
    tx_date     datetime NOT NULL,
    PRIMARY KEY (id)
)