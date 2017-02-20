Power Jack Database

Create database JPBase;

use JPBase;

create table location(
id int not null auto_increment,
light int,
name varchar(25),
description varchar(2000),
primary key(id)
);

create table Map(
locationid int,
ctu tinyint,
prison tinyint,
pub tinyint,
itis tinyint,
mp tinyint,
castle tinyint,
warehouse tinyint,
warein tinyint,
kauppatori tinyint,
pippuri tinyint,
fp tinyint,
kamppi tinyint,
foreign key (locationid) references location(id)
);

create table item(
id int not null auto_increment,
name varchar(25),
primary key(id)
);

create table wearable(
itemid int,
attention int,
foreign key (itemid) references item(id)
);

create table useable(
itemid int,
sound tinyint,
dmg tinyint,
distance int,
dark tinyint,
foreign key (itemid) references item(id)
);


create table npc(
id int not null auto_increment,
happiness int,
locationid int,
itemid int,
primary key (id),
foreign key (locationid) references location(id),
foreign key (itemid) references item(id)
);

create table jack(
id int not null auto_increment,
attention int,
addiction int,
locationid int,
name varchar(25),
itemid int,
primary key(id),
foreign key(itemid) references item(id),
foreign key(locationid) references location(id)
);