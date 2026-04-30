# rbs_inline: enabled

module LetterInspection
  class Application
    # @rbs source: String
    # @rbs target: String
    # @rbs return: bool
    def self.exactly_equal_size_and_included?(source:, target:)
      new(source, target).exactly_equal_size_and_included?
    end

    # @rbs source: String
    # @rbs target: String
    # @rbs return: void
    def initialize(source, target)
      @source = source
      @target = target
    end

    # @rbs return: bool
    def exactly_equal_size_and_included?
      sort_string(source) == sort_string(target)
    end

    private

    attr_reader :source, :target

    # @rbs str: String
    # @rbs return: String
    def sort_string(str)
      str.split('').sort.join('')
    end
  end
end
