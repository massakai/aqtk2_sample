# Macでビルドする設定
EXEC=aqtk2_example
SRC=main.cpp
FRAMEWORK_DIR=.
AQUES_TALK2=AquesTalk2Eva

.PHONY: run build clean

run: build
	./$(EXEC)

build: $(EXEC) $(EXEC2)

clean:
	rm -f $(EXEC) *.wav

$(EXEC): $(SRC)
	g++ -I$(FRAMEWORK_DIR)/$(AQUES_TALK2).framework/Headers \
	    -F$(FRAMEWORK_DIR) -framework $(AQUES_TALK2) -o $@ $+
