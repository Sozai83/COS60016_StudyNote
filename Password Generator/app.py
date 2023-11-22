from flask import Flask, redirect, url_for, render_template, request
import requests
from random import randint

def password_generator_01(max_length, allowed_chars, seed=None):
    if max_length < 10:
        raise Exception("Password cannot be shorter then 10")
    if seed:
         random.seed(seed)