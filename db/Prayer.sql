PGDMP         	        	        {            Prayer    15.2    15.2     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16896    Prayer    DATABASE        CREATE DATABASE "Prayer" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE "Prayer";
                postgres    false            �            1259    16898 	   pr_prayer    TABLE     s   CREATE TABLE public.pr_prayer (
    id integer NOT NULL,
    name text,
    address text,
    denomination text
);
    DROP TABLE public.pr_prayer;
       public         heap    postgres    false            �            1259    16897    prayer_prayerid_seq    SEQUENCE     �   CREATE SEQUENCE public.prayer_prayerid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.prayer_prayerid_seq;
       public          postgres    false    215            �           0    0    prayer_prayerid_seq    SEQUENCE OWNED BY     H   ALTER SEQUENCE public.prayer_prayerid_seq OWNED BY public.pr_prayer.id;
          public          postgres    false    214            e           2604    16901    pr_prayer id    DEFAULT     o   ALTER TABLE ONLY public.pr_prayer ALTER COLUMN id SET DEFAULT nextval('public.prayer_prayerid_seq'::regclass);
 ;   ALTER TABLE public.pr_prayer ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    215    215            �          0    16898 	   pr_prayer 
   TABLE DATA           D   COPY public.pr_prayer (id, name, address, denomination) FROM stdin;
    public          postgres    false    215   �
       �           0    0    prayer_prayerid_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.prayer_prayerid_seq', 3, true);
          public          postgres    false    214            g           2606    16905    pr_prayer prayer_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.pr_prayer
    ADD CONSTRAINT prayer_pkey PRIMARY KEY (id);
 ?   ALTER TABLE ONLY public.pr_prayer DROP CONSTRAINT prayer_pkey;
       public            postgres    false    215            �   �   x��M� ��p�ٹQS4iz7_;S)~4�^��,=�M�'m���^�����/���H�w��hm�dn�r�J��4'^O	�-:ۙ]�(��Z���@��3�E���.���@G�Q�c��/@     