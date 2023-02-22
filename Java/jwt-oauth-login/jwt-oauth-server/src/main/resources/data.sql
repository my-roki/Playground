INSERT INTO members (MEMBER_ID, EMAIL, USERNAME) SELECT 1, 'user01@hello.com', 'user01' FROM DUAL WHERE NOT EXISTS(SELECT true FROM members WHERE MEMBER_ID = 1);
INSERT INTO members (MEMBER_ID, EMAIL, USERNAME) SELECT 2, 'user02@hello.com', 'user02' FROM DUAL WHERE NOT EXISTS(SELECT true FROM members WHERE MEMBER_ID = 2);
INSERT INTO members (MEMBER_ID, EMAIL, USERNAME) SELECT 3, 'user03@hello.com', 'user03' FROM DUAL WHERE NOT EXISTS(SELECT true FROM members WHERE MEMBER_ID = 3);

INSERT INTO members_roles (MEMBERS_MEMBER_ID, ROLES) SELECT 1, 'USER' FROM DUAL WHERE NOT EXISTS(SELECT true FROM members_roles WHERE MEMBERS_MEMBER_ID = 1);
INSERT INTO members_roles (MEMBERS_MEMBER_ID, ROLES) SELECT 2, 'USER' FROM DUAL WHERE NOT EXISTS(SELECT true FROM members_roles WHERE MEMBERS_MEMBER_ID = 2);
INSERT INTO members_roles (MEMBERS_MEMBER_ID, ROLES) SELECT 2, 'USER' FROM DUAL WHERE NOT EXISTS(SELECT true FROM members_roles WHERE MEMBERS_MEMBER_ID = 3);