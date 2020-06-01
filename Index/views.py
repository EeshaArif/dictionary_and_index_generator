
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template.loader import get_template
from string import ascii_lowercase
import re
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string

from fpdf import FPDF, HTMLMixin


# Create your views here.

class HtmlPdf(FPDF, HTMLMixin):
    pass


# node object for tree data structure
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)


def index(request):
    return render(request, 'home.html')


def index_c(request):
    if request.method == 'POST':

        if "index_gen" in request.POST:
            filepath = request.FILES.get('file', False)
            if filepath:
                text = request.FILES['file'].read()
                encoding = 'utf-8'
                new_text = str(text, encoding)
                num_of_lines = new_text.split("\n")

                # get words
                words = {}
                for j in range(1, len(num_of_lines) + 1):
                    words[j] = num_of_lines[j - 1]
                    words[j] = words[j].split()

                common_words = ['this', 'is', 'a', 'the', 'they', 'did', 'not', 'at', 'be', 'so', 'in', 'and',
                                'etc', 'in', 'its', 'it', 'of', 'The', 'This', 'Then', 'was', 'them', 'Them', 'all', 'All',
                                'also', 'Also', 'can', 'do', 'etc', 'get', 'in', 'on', 'or', 'to', 'use', 'with', 'which',
                                'You', 'you', 'would', 'an', 'as', 'As', 'been', 'but', 'come', 'from', 'for', 'he', 'I',
                                'what', 'when', 'where', 'here', 'want', 'wants', 'had', 'have', 'up', 'using', 'used', 'A',
                                'are', 'by', 'If', 'if', 'In', 'will', 'we', 'We', 'that', 'his', 'it', 'It', 'those', 'their'
                                , 'then', 'has', 'any']

                # Create Tree Data Structure
                start = Node("Text")  # head node

                # fill tree with words
                for c in ascii_lowercase:
                    for i in range(1, len(num_of_lines) + 1):
                        for l in range(0, len(words[i])):
                            if (words[i][l][0] == c.upper() or words[i][l][0] == c) and (words[i][l] not in common_words):
                                if c.upper() in [o.data for o in start.children] or c in [o.data for o in start.children]:
                                    new_word_node = Node(words[i][l])
                                    for adding in start.children:
                                        if adding.data == c.upper() or adding.data == c:
                                            adding.add_child(new_word_node)
                                    new_word_node.add_child(Node(i))
                                else:
                                    new_alpha_node = Node(c.upper())
                                    start.add_child(new_alpha_node)
                                    new_word_node_2 = Node(words[i][l])
                                    new_alpha_node.add_child(new_word_node_2)
                                    new_word_node_2.add_child(Node(str(i)))

                # sort tree alphabetically
                for to_sort in start.children:
                    to_sort.children.sort(key=lambda x: x.data, reverse=False)

                # print tree to output html

                counter = 0
                list = []
                for p in start.children:
                    list.insert(counter, str(p.data))
                    counter = counter + 1
                    for t in p.children:
                        for yu in t.children:
                            list.insert(counter, str(t.data) + ("." * (90 - len(str(t.data)))) + str(yu.data))
                            counter = counter + 1

                alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                         'U', 'V', 'W', 'X', 'Y', 'Z']
                return render(request, 'index_output.html', {'list': list, "alpha": alpha})

        if "dic_gen" in request.POST:
            filepath = request.FILES.get('file', False)
            if filepath:
                text = request.FILES['file'].read()
                encoding = 'utf-8'
                new_text = str(text, encoding)
                num_of_lines = new_text.split("\n")
                # get words
                words = {}
                for j in range(1, len(num_of_lines) + 1):
                    words[j] = num_of_lines[j - 1]
                    words[j] = words[j].split()

                common_words = ['this', 'is', 'a', 'the', 'they', 'did', 'not', 'at', 'be', 'so', 'in', 'and',
                                'etc', 'in', 'its', 'it', 'of', 'The', 'This', 'Then', 'was', 'them', 'Them', 'all', 'All',
                                'also', 'Also', 'can', 'do', 'etc', 'get', 'in', 'on', 'or', 'to', 'use', 'with', 'which',
                                'You', 'you', 'would', 'an', 'as', 'As', 'been', 'but', 'come', 'from', 'for', 'he', 'I',
                                'what', 'when', 'where', 'here', 'want', 'wants', 'had', 'have', 'up', 'using', 'used', 'A',
                                'are', 'by', 'If', 'if', 'In', 'will', 'we', 'We', 'that', 'his', 'it', 'It', 'those', 'their'
                                , 'then', 'has', 'any']

                # Create Tree Data Structure
                start = Node("Text")  # head node

                # fill tree with words
                for c in ascii_lowercase:
                    for i in range(1, len(num_of_lines) + 1):
                        for l in range(0, len(words[i])):
                            if (words[i][l][0] == c.upper() or words[i][l][0] == c) and (words[i][l] not in common_words):
                                if c.upper() in [o.data for o in start.children] or c in [o.data for o in start.children]:
                                    new_word_node = Node(words[i][l])
                                    for adding in start.children:
                                        if adding.data == c.upper() or adding.data == c:
                                            adding.add_child(new_word_node)
                                    new_word_node.add_child(Node(i))
                                else:
                                    new_alpha_node = Node(c.upper())
                                    start.add_child(new_alpha_node)
                                    new_word_node_2 = Node(words[i][l])
                                    new_alpha_node.add_child(new_word_node_2)
                                    new_word_node_2.add_child(Node(str(i)))

                # sort tree alphabetically
                for to_sort in start.children:
                    to_sort.children.sort(key=lambda x: x.data, reverse=False)

                # remove duplicate for dictionary
                record = set()
                result = []
                for dup in start.children:
                    for dup2 in dup.children:
                        if dup2.data not in record:
                            record.add(dup2.data)
                            result.append(dup2)

                # print tree to output html
                counter = 0
                list = []
                for p in result:
                    if counter >= 2:
                        if list[counter - 1][0] == str(p.data[0]) or list[counter - 1][0] == str(p.data[0].upper()):
                            list.insert(counter, str(p.data))
                            counter = counter + 1
                        else:
                            list.insert(counter, str(p.data[0].upper()))
                            counter = counter + 1
                            list.insert(counter, str(p.data))
                            counter = counter + 1
                    elif counter == 0 or counter == 1:
                        list.insert(counter, str(p.data[0].upper()))
                        counter = counter + 1
                        list.insert(counter, str(p.data))
                        counter = counter + 1

                alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                         'U', 'V', 'W', 'X', 'Y', 'Z']
                return render(request, 'dic_output.html', {'list': list, "alpha": alpha})

    return render(request, 'index_c.html')


def index_output(request):
    return render(request, 'index_output.html')


def dic_output(request):
    return render(request, 'dic_output.html')


class GenPDF(TemplateView):
    def get(self, request, *args, **kwargs):
        template = get_template("index_output.html")

        return template.render
