module LetterInspection
  class Application
    def self.exactly_equal_size_and_included?(source:, target:)
      new(source, target).exactly_equal_size_and_included?
    end

    def initialize(source, target)
      @source = source
      @target = target
    end

    def exactly_equal_size_and_included?
      sort_string(source) == sort_string(target)
    end

    private

    attr_reader :source, :target

    def sort_string(str)
      str.split('').sort.join('')
    end
  end
end
