module LetterInspection
  class Application
    def initialize(str_1, str_2)
      @str_1 = str_1
      @str_2 = str_2
    end

    def exactly_equal_size_and_included?
      sort_string(str_1) == sort_string(str_2)
    end

    private

    attr_reader :str_1, :str_2

    def sort_string(str)
      str.split('').sort.join('')
    end
  end
end
